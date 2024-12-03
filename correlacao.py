from flask import Flask, render_template_string
import pandas as pd

excel = pd.read_excel("correlacao.xlsx")

app = Flask(__name__)

@app.route('/')
def show_table():
    table_html = excel.to_html(index=False, classes="table table-bordered")
    return render_template_string('''
        <html>
        <head>
            <title>Bitcoin e Ethereum</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f8f9fa;
                    color: #333;
                }
                h1 {
                    text-align: center;
                    padding: 20px;
                    background-color: #007bff;
                    color: white;
                    margin-bottom: 20px;
                }
                .table {
                    width: 80%;
                    margin: 0 auto;
                    border-collapse: collapse;
                    background-color: white;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                .table th, .table td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: center;
                }
                .table th {
                    background-color: #007bff;
                    color: white;
                    font-weight: bold;
                }
                .table tr:nth-child(even) {
                    background-color: #f2f2f2;
                }
                .table tr:hover {
                    background-color: #ddd;
                }
            </style>
        </head>
        <body>
            <h1>BITCOIN - ETHEREUM</h1>
            {{ table_html | safe }}
        </body>
        </html>
    ''', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
