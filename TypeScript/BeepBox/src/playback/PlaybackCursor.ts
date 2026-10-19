export class PlaybackCursor {


    beat:number;


    bar:number;


    playing:boolean;



    constructor(){

        this.beat=0;

        this.bar=0;

        this.playing=false;

    }




    reset(){

        this.beat=0;

        this.bar=0;

    }




    moveTo(
        beat:number
    ){

        this.beat=beat;


        this.bar =
        Math.floor(
            beat / 4
        );

    }




    advance(
        amount:number
    ){

        this.moveTo(
            this.beat + amount
        );

    }



}