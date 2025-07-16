const data = require('./data_reader.js');

/**
 * Goes through the JSON data and counts the amount of messages sent per user, adding them to the users dictionary if
 * they aren't already on there.
 *
 * @param raw_messages_data_json The JSON data about the message history.
 * @param user_message_count The users dictionary to store data in
 */
function extract_message_counts(raw_messages_data_json, user_message_count) {
    raw_messages_data_json.forEach((message) => {
        const encoded_name = message.sender_name;
        if (encoded_name in user_message_count) {
            user_message_count[encoded_name].count++;
        } else {
            user_message_count[encoded_name] = {
                name: data.decode_username(encoded_name),
                count: 1
            };
        }
    });
    return user_message_count;
}

/**
 * This will find all data files in the /data/ directory, fetch the JSON from them and run them through the analysis
 * to get how many messages each user has sent.
 *
 * @returns A promise of a dictionary of all the encoded usernames against their decoded username and the messages sent.
 */
function compile_data() {
    let users = {}
    const data_analysis_promises = []
    data.fetch_all_data_files('data/').forEach((file_url) => {
        data_analysis_promises.push(data.get_message_data(`data/${file_url}`));
    })

    return new Promise((resolve, reject) => {
        Promise.all(data_analysis_promises).then(file_data => {
            file_data.forEach(data => {
                users = extract_message_counts(data.messages, users);
            })
            resolve(users);
        });
    });
}

compile_data().then(data => {
    console.log(data);
})