$filepath="$(pwd)"
function activate {
    cd $filepath
    pwd
    py -m venv sierpinski-triangle-venv
    ."\sierpinski-triangle-venv\Scripts\Activate.ps1"
    py -m pip install --upgrade pip
    py -m pip install -r requirements.txt
}
activate
