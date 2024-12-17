from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def page():
    return render_template('index.html')

@app.route('/proccess', methods=['POST'])
def proccess():
    form = request.form

    grev  = float(form['grev'])
    greq  = float(form['greq'])
    toefl = float(form['toefl'])
    cgpa  = float(form['cgpa'])

    df = pd.read_csv('static/Processed_data.csv')
    print(df)

    # Fitur untuk KNN
    features = df.drop(columns='univName').values

    user_input = [grev, greq, toefl, cgpa]
    print(user_input)

    # Mendapatkan rekomendasi
    output = knn(df, features, user_input, n_neighbors=7)

    # Menampilkan hasil
    print("Top 5 Rekomendasi Universitas dengan Probabilitas:")
    print(output)
    
    return render_template("hasill.html",output=output)

# Fungsi menghitung jarak Euclidean
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2, axis=1))

# Implementasi KNN
def knn(df, features, user_input, n_neighbors):
    distances = euclidean_distance(features, user_input)
    indices = np.argsort(distances)[:n_neighbors]
    nearest_distances = distances[indices]
    
    # Menghitung probabilitas (normalisasi jarak)
    probabilities = 1 - (nearest_distances / np.max(nearest_distances))
    probabilities /= probabilities.sum()  # Normalisasi agar total probabilitas = 1

    recommendations = df.iloc[indices].copy()
    recommendations["probability"] = probabilities
    recommendations["probability"] = recommendations["probability"].round(5)  # Mengatur angka di belakang koma
    recommendations = recommendations[recommendations["probability"] > 0]  # Filter probabilitas > 0
    return recommendations[["univName", "probability"]]
    
if __name__ == "__main__":
    app.run(debug=True)