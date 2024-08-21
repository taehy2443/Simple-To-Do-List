from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# 데이터베이스 초기화
def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, status INTEGER)''')
    conn.commit()
    conn.close()

# 홈 페이지
@app.route('/')
def home():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# 할 일 추가
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute('INSERT INTO tasks (task, status) VALUES (?, 0)', (task,))
        conn.commit()
        conn.close()
    return redirect('/')

# 할 일 완료
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('UPDATE tasks SET status = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect('/')

# 할 일 삭제
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()  # 애플리케이션 시작 시 데이터베이스 초기화
    app.run(debug=True)