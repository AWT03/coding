const readline = require('readline');
const fs = require('fs');

const number_0 = " _ " +
                 "| |" +
                 "|_|";
const number_1 = "   " +
                 "  |" +
                 "  |";
const number_2 = " _ " +
                 " _|" +
                 "|_ ";
const number_3 = " _ " +
                 " _|" +
                 " _|";
const number_4 = "   " +
                 "|_|" +
                 "  |";
const number_5 = " _ " +
                 "|_ " +
                 " _|";
const number_6 = " _ " +
                 "|_ " +
                 "|_|";
const number_7 = " _ " +
                 "  |" +
                 "  |";
const number_8 = " _ " +
                 "|_|" +
                 "|_|";
const number_9 = " _ " +
                 "|_|" +
                 " _|";

const translator = {};
translator[number_0] = "0";
translator[number_1] = "1";
translator[number_2] = "2";
translator[number_3] = "3";
translator[number_4] = "4";
translator[number_5] = "5";
translator[number_6] = "6";
translator[number_7] = "7";
translator[number_8] = "8";
translator[number_9] = "9";

async function get_numbers(file){
    let numbers = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''};
    let index = 0;
    await new Promise((resolve) => {
        file.on('line', async (line) => {
            index = 0;
            for (let i=0; i<27; i+=3){
                if (line.substring(i, i+3)){
                    numbers[index] += line.substring(i, i+3);
                    for (let j=0; j<(3-line.substring(i, i+3).length); j++){
                        numbers[index] += " ";
                    }
                } else {
                    numbers[index] += "   ";
                }
                index+=1;
            }
            resolve(numbers);
        });
    });
    return numbers
}

async function translate_numbers(numbers){
    let account_number = '';
    return new Promise((resolve)=>{
        for (let i=0; i<9; i++) {
            if (numbers[i] in translator){account_number += translator[numbers[i]]}
            else{account_number += '?'}
        }
        resolve(account_number);
    });
}


function do_rotation(number){
    let list_possible = [];
    for (let i=0; i<number.length; i++){
        let possible = number.split('');
        ["_", " ", "|"].forEach( (item) => {
            possible[i] = item;
            if (possible.join('') in translator){
                list_possible.push(translator[possible.join('')]);
            }
        });
    }
    return [...new Set(list_possible)]
}

async function get_values(numbers, index){
    let account_number = await translate_numbers(numbers);
    let possible_values = [];
    do_rotation(numbers[index]).forEach(async (option) => {
        let possible = account_number.split('');
        possible[index] = option;
        let valid_account_number = await validate_account_number(possible.join(''));
        if (valid_account_number){
            possible_values.push(possible.join(''))
        }
    });
    return possible_values
}

//User Story #1
async function read_file(file_path){
    const readInterface = await readline.createInterface({
        input: fs.createReadStream(file_path)
    });
    return await translate_numbers(await get_numbers(readInterface));
}

//User Story #2
async function validate_account_number(account_number){
    if (account_number.includes("?")){
        return false
    }
    let checksum = 0;
    for (let i=0; i<account_number.length; i++){
        checksum += Number(account_number[i]) * (9-i)
    }
    return checksum % 11 === 0
}

//User Story #3
async function get_status(file_path){
    let account_number = await read_file(file_path);
    if (account_number.includes('?')){return account_number + ' ILL'}
    else if (!validate_account_number(account_number)) {return account_number + ' ERR'}
    else {return account_number}
}

// User Story #4
async function get_possibles(file_path){
    const readInterface = await readline.createInterface({
        input: fs.createReadStream(file_path)
    });
    let numbers = await get_numbers(readInterface);
    let account_number = await translate_numbers(numbers);
    let possible_values = [];
    return new Promise(async (resolve) => {
        let valid_account_number = await validate_account_number(account_number);
        if (!valid_account_number || account_number.includes('?')){
            for (let i=0; i<account_number.length; i++){
                let new_values = await get_values(numbers, i);
                possible_values = possible_values.concat(new_values);
            }
        }
        if (!possible_values){
            resolve(account_number + "ILL")
        } else if (possible_values.length === 1){
            resolve(possible_values[0])
        } else {
            resolve(account_number + " AMB ['" +
                possible_values.sort().join("', '") + "']")
        }
    });
}

module.exports = {
    read_file,
    validate_account_number,
    get_status,
    get_possibles
};
