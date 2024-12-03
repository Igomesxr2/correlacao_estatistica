from flask import Flask, render_template_string
import pandas as pd

excel = pd.read_excel("correlacao.xlsx")

numeric_data = excel.select_dtypes(include=['number'])

if numeric_data.shape[1] >= 2:
    correlacao_valor = numeric_data.iloc[:, 0].corr(numeric_data.iloc[:, 1])
else:
    correlacao_valor = None

app = Flask(__name__)

@app.route('/')
def show_table():

    table_html = excel.to_html(index=False, classes="table table-bordered")
    
    if correlacao_valor is not None:
        correlacao_msg = f"A correlação é: {correlacao_valor:.2f}"
    else:
        correlacao_msg = "Não foi possível calcular a correlação, pois não há pelo menos duas colunas numéricas."
    
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
                .correlation {
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                    font-weight: bold;
                    color: #007bff;
                }
            </style>
        </head>
        <body>
            <h1>BITCOIN - ETHEREUM</h1>
            {{ table_html | safe }}
            <p class="correlation">{{ correlacao_msg }}</p>
        </body>
        </html>
    ''', table_html=table_html, correlacao_msg=correlacao_msg)

if __name__ == '__main__':
    app.run(debug=True)
