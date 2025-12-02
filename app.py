from flask import Flask, render_template, url_for, session, redirect

app = Flask(__name__)
app.secret_key = "asjgddu1d91n01f9*@102490c(*@*&#@)fWIADHA"

def check_winner(board):
    # These are the 8 ways to win (Indices 0-8)
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]

    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


@app.route('/')
def index():
    if 'board' not in session:
        session['board'] = [" "] * 9
        session['turn'] = "X"
        session['winner'] = None
    return render_template('index.html', game=session)

@app.route('/press/<int:index>', methods=['POST'])
def press(index):
    if session.get('winner'):
        return redirect(url_for('index'))
    
    board = session['board']

    if board[index] == " ":
        board[index] = session['turn']
        session['board'] = board

        winner = check_winner(board)

        if winner:
            session['winner'] = winner
        else:
            if session['turn'] == "X":
                session['turn'] = "O"
            else:
                session['turn'] = "X"
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)