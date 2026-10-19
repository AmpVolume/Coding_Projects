export class Timeline {


    bpm:number;


    beatsPerMeasure:number;


    currentBeat:number;



    constructor(
        bpm:number = 120
    ){

        this.bpm=bpm;

        this.beatsPerMeasure=4;

        this.currentBeat=0;

    }



    secondsPerBeat():number{

        return 60 / this.bpm;

    }



    beatToSeconds(
        beat:number
    ):number{

        return beat*this.secondsPerBeat();

    }



}