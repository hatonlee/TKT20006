from flask import Flask, request, render_template, redirect, url_for
from siirto import Siirto
from ksp import KspPelaajaVsPelaaja, KspYksinkertainenTekoaly, KspKehittynytTekoaly

app = Flask(__name__)

# Persistent game instances (live until server restart)
games = {
    'pvp': KspPelaajaVsPelaaja(),
    'simple': KspYksinkertainenTekoaly(),
    'advanced': KspKehittynytTekoaly(),
}


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/mode/<mode>', methods=['GET', 'POST'])
def mode_page(mode: str):
    mode = mode.lower()
    if mode not in games:
        return redirect(url_for('index'))

    game = games[mode]

    if request.method == 'POST':
        # Process submission
        if mode == 'pvp':
            move1 = request.form.get('move1', '').strip()
            move2 = request.form.get('move2', '').strip()
            try:
                eka = Siirto.from_str(move1)
                toka = Siirto.from_str(move2)
            except Exception as e:
                return render_template('pvp.html', game=game, error=str(e))
            # Update game state
            game.pelaa_siirrot(eka, toka)
            return render_template('pvp.html', game=game)

        else:
            move1 = request.form.get('move1', '').strip()
            try:
                eka = Siirto.from_str(move1)
            except Exception as e:
                template = 'simple.html' if mode == 'simple' else 'advanced.html'
                return render_template(template, game=game, error=str(e))

            # For AI games use their helper method which returns (toka, tuomari_str)
            game.pelaa_eka(eka)
            template = 'simple.html' if mode == 'simple' else 'advanced.html'
            return render_template(template, game=game)

    # GET request
    template = 'pvp.html' if mode == 'pvp' else ('simple.html' if mode == 'simple' else 'advanced.html')
    return render_template(template, game=game)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
