function solution(record) {
    var answer = [];
    var res = [];
    var stat = {'Enter': 'Came in','Leave': 'has left'}
    var user = {};

    for(i=0; i<record.length; i++){
        res.push(record[i].split(" "));
        if (res[i][2] != undefined){
            user[res[i][1]] = res[i][2]
        }
    }

    for(i=0; i<res.length; i++){
        var x = stat[res[i][0]]
        var y = user[res[i][1]]
        if ((x && y) != undefined){
            answer.push(y + ' ' + x)
        }
    }

    console.log(answer);
    //return answer;
}

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan", "Leave uid4567", "Change uid1234 Chandra", "Enter uid4567 Anton"]);