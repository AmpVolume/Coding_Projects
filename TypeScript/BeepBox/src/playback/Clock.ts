export class Clock {


    bpm:number;

    startTime:number;

    running:boolean;



    constructor(
        bpm:number = 120
    ){

        this.bpm=bpm;

        this.startTime=0;

        this.running=false;

    }





    start(){

        this.startTime =
        performance.now();

        this.running=true;

    }





    stop(){

        this.running=false;

    }





    getTime():number{


        if(!this.running)
            return 0;



        return (
            performance.now()
            -
            this.startTime
        ) / 1000;

    }





    secondsPerBeat():number{

        return 60 / this.bpm;

    }





    getBeat():number{


        return (
            this.getTime()
            /
            this.secondsPerBeat()
        );


    }




}