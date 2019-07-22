//You can run this test with mocha
//install it gobally with "npm install --global mocha"
//then open folder with this file and run "mocha test.js"
const {read_file, validate_account_number, get_status, get_possibles} = require('./gabriel');
const assert = require('assert');


// User Story #1
it('test case 00', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_00.txt'),
        "000000000")
});

it('test case 01', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_01.txt'),
        "111111111")
});

it('test case 02', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_02.txt'),
        "222222222")
});

it('test case 03', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_03.txt'),
        "333333333")
});

it('test case 04', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_04.txt'),
        "444444444")
});

it('test case 05', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_05.txt'),
        "555555555")
});

it('test case 06', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_06.txt'),
        "666666666")
});

it('test case 07', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_07.txt'),
        "777777777")
});

it('test case 08', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_08.txt'),
        "888888888")
});

it('test case 09', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_09.txt'),
        "999999999")
});

it('test case 10', async () => {
    assert.strictEqual(await read_file(__dirname + '/test_cases/test_case_10.txt'),
        "123456789")
});

// User Story #2
it('test valid account number', async ()=> {
    assert.strictEqual(await validate_account_number("457508000"), true)
});

it('test invalid account number', async ()=> {
    assert.strictEqual(await validate_account_number("664371495"), false)
});

// User Story #3
it('test case 11', async () => {
    assert.strictEqual(await get_status(__dirname + '/test_cases/test_case_11.txt'),
        "000000051")
});

it('test case 12', async () => {
    assert.strictEqual(await get_status(__dirname + '/test_cases/test_case_12.txt'),
        "49006771? ILL")
});

it('test case 13', async () => {
    assert.strictEqual(await get_status(__dirname + '/test_cases/test_case_13.txt'),
        "1234?678? ILL")
});

// User Story #4
it('test case 14', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_14.txt'),
        "711111111")
});

it('test case 15', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_15.txt'),
        "777777177")
});

it('test case 16', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_16.txt'),
        "200800000")
});

it('test case 17', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_17.txt'),
        "333393333")
});

it('test case 18', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_18.txt'),
        "888888888 AMB ['888886888', '888888880', '888888988']")
});

it('test case 19', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_19.txt'),
        "555555555 AMB ['555655555', '559555555']")
});

it('test case 20', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_20.txt'),
        "666666666 AMB ['666566666', '686666666']")
});

it('test case 21', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_21.txt'),
        "999999999 AMB ['899999999', '993999999', '999959999']")
});

it('test case 22', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_22.txt'),
        "490067715 AMB ['490067115', '490067719', '490867715']")
});

it('test case 23', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_23.txt'),
        "123456789")
});

it('test case 24', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_24.txt'),
        "000000051")
});

it('test case 25', async () => {
    assert.strictEqual(await get_possibles(__dirname + '/test_cases/test_case_25.txt'),
        "490867715")
});
