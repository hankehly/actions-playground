const core = require("@actions/core");
const exec = require("@actions/exec");


// most @actions toolkit packages have async methods
async function run() {
    try {
        // const version = core.getInput('version');
        await exec.exec('curl -O -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py');
        await exec.exec('python get-poetry.py --preview');
        core.addPath(`${process.env.HOME}/.poetry/bin`);
    } catch (error) {
        core.setFailed(error.message);
    }
}

run();
