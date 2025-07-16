const fs = require('fs');
const path = require('path');

/**
 * Takes in a file URL, opens the file at that location and parses it to JSON and returns said JSON value.
 *
 * @param file_path The string path of the file URL to fetch the JSON from.
 * @returns A JSON representation of the data stored in the file.
 */
async function get_message_data(file_path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path.resolve(__dirname, file_path), 'utf-8', function (err, data) {
            if (err) throw err;
            resolve(JSON.parse(data));
        });
    });
}

/**
 * Instagram data returns double-encoded unicode strings, and genuine text may be presented as just \\u00xx, and looks
 * even worse when printed to the console where it may just appear as spaces - this will convert it to latin1 and
 * decode back from utf-8 to fix this.
 *
 * @param encoded_username The username encoded with \\u00xx codes that needs converting.
 * @returns A clean string showing what the user would've seen in the Instagram app.
 */
function decode_username(encoded_username) {
    return new TextDecoder('utf-8').decode(new Uint8Array([...encoded_username].map(c => c.charCodeAt(0))));
}

/**
 * Instagram splits data into different JSON files, this will get all the file names that need to be analysed for a
 * complete analysis.
 *
 * @param directory The directory to look through.
 * @returns A list of file names in the given directory location.
 */
function fetch_all_data_files(directory) {
    return fs.readdirSync(path.resolve(__dirname, directory));
}

module.exports = {get_message_data, decode_username, fetch_all_data_files};