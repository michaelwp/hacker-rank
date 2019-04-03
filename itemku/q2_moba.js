function solution(N, users) {
    // set the variables
    var answer = [];
    var i = 0; //stage level
    var u = 0; //number of users in or up of current stage
    var f = 0; //number of users in current stage

    //count the failure rate
    while(i < N){
        i++;
        for(var j in users){
            if(users[j] >= i){
                u++;
            }
            
            if(users[j] == i){
                f++;
            } 
        }
        answer.push([i, (f/u)]);
        u = 0;
        f = 0;
    }
    
    //sorting answer
    answer.sort((stage, fRate) => fRate[1] - stage[1]);

    //pick the stage only
    for(a in answer){
        answer[a] = answer[a][0];
    }

    //return the answer
    return answer;
}