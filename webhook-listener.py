from flask import Flask, request
import subprocess

app = Flask(__name__)

# Endpoint untuk menerima request POST dari GitHub
@app.route('/deploy', methods=['POST'])
def deploy():
    # Verifikasi bahwa request berasal dari GitHub (opsional)
    if request.headers.get('X-GitHub-Event') == 'push':
        # Menjalankan deploy.sh setiap kali menerima webhook
        subprocess.call(['/var/www/html/CloneSIPINTAR/deploy.sh'])
        return 'Deploy berhasil!', 200
    else:
        return 'Request tidak valid!', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
