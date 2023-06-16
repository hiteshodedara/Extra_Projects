const buttonColors = [`red`, `blue`, `green`, `yellow`];
let gamePattern = [];
let userClickedPattern = [];
let level = 0;
let started = false;

// $(document).ready(nextSequence);

$(document).keypress(function(){
    if(!started){
        $(`#level-title`).text(`Level `+ level);
        nextSequence();
        started = true;
    }
});

function checkAnswer(currentLevel){
    if(gamePattern[currentLevel] === userClickedPattern[currentLevel]){
        console.log(`Success`);
        if(userClickedPattern.length === gamePattern.length){
            setTimeout(() => {
                nextSequence();
            }, 1000);
        }
    }
    else{
        console.log(`Wrong`);
        gameOver();
        restart();
    }
}

$(`.btn`).click(function(){
    let userChosenColor = $(this).attr(`id`);
    userClickedPattern.push(userChosenColor);
    playSound(userChosenColor);
    animatePress(userChosenColor);
    checkAnswer(userClickedPattern.length-1);
});

function nextSequence(){
    userClickedPattern=[];
    level++;
    $(`#level-title`).text(`Level `+ level);
    let randomNumber = Math.floor(Math.random()*4);
    let randomChosenColor = buttonColors[randomNumber];
    gamePattern.push(randomChosenColor);
    console.log(gamePattern);
    $(`#` + randomChosenColor).fadeOut(50).fadeIn(50);
    playSound(randomChosenColor);
    checkAnswer();
}

function playSound(name){
    var audio = new Audio(`sounds/` + name + `.mp3`);
    audio.play();
}

function animatePress(currentColor){
    $(`#`+currentColor).addClass(`pressed`);
    setTimeout(() => {
        $(`#`+currentColor).removeClass(`pressed`);
    }, 100);
};

function gameOver(){
    playSound(`wrong`);
    $(`body`).addClass(`game-over`);
    setTimeout(() => {
        $(`body`).removeClass(`game-over`);
    }, 200);
    $(`#level-title`).text(`Game Over, Press Any Key to Restart`);
}

function restart(){
    level = 0;
    gamePattern = [];
    started = false;
}




