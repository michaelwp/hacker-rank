
function solution(record) {
    //set the variables
    var answer = [];
    var res = []; //list of words parsed in record
    var stat = {'Enter': 'Came in',
                'Leave': 'has left'} //user status dictionary
    var user = {}; //list of user in the chat room

    //parsing record and capturing the user inside
    for (var i in record){
        res.push(record[i].split(" "));
        if (res[i][2] != undefined){
            user[res[i][1]] = res[i][2]
        }
    }

    //set the answer
    for (var i in res){
        var x = stat[res[i][0]]
        var y = user[res[i][1]]
        if ((x && y) != undefined){
            answer.push(y + ' ' + x)
        }
    }

    //return the answer;
    return answer;
}