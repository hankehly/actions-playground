import os from 'os';
import path from 'path';

import * as core from '@actions/core';
import { exec } from '@actions/exec';


// most @actions toolkit packages have async methods
async function run() {
    try {
        // const version = core.getInput('version');
        await exec('curl -O -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py');
        await exec('python get-poetry.py --preview');
        core.addPath(path.join(os.homedir(), '.poetry', 'bin'));
    } catch (error) {
        core.setFailed(error.message);
    }
}

run();
