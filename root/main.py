import os
import subprocess


def installs():
    venv_path = "virtualis_kornyezet"
    scripts_path = os.path.join(venv_path, "Scripts")
    pip_path = os.path.join(scripts_path, "pip")
    python_path = os.path.join(scripts_path, "python")

    subprocess.run("pip install virtualenv", shell=True)
    subprocess.run("virtualenv " + venv_path, shell=True)
    subprocess.run(f"{pip_path} install -r .\\requirements.txt", shell=True)
    subprocess.run([python_path, "./kezdoOldal.py"], shell=True)
    

def start():
    venv_path = "virtualis_kornyezet"
    scripts_path = os.path.join(venv_path, "Scripts")
    python_path = os.path.join(scripts_path, "python")
    subprocess.run([python_path, "./kezdoOldal.py"], shell=True)

def check_packages():
    with open("FONTOS.txt", "r+", encoding="UTF-8") as fajl:
        elso_sor = fajl.readline().strip()
        if elso_sor == "a_csomagok_NINCSENEK_telepitve":
            installs()
            fajl.seek(0)
            fajl.write("a_csomagok_telepitve")
            fajl.truncate()
        else:
            start()


check_packages()
