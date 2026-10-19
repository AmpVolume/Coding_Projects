export class Envelope {


    attack:number;

    decay:number;

    sustain:number;

    release:number;



    constructor(){

        this.attack = 0.01;

        this.decay = 0.2;

        this.sustain = 0.7;

        this.release = 0.5;

    }




    apply(
        gain:GainNode,
        time:number,
        duration:number
    ){


        const param =
            gain.gain;



        param.cancelScheduledValues(time);



        param.setValueAtTime(
            0,
            time
        );


        param.linearRampToValueAtTime(
            1,
            time + this.attack
        );



        param.linearRampToValueAtTime(
            this.sustain,
            time +
            this.attack +
            this.decay
        );



        param.setValueAtTime(
            this.sustain,
            time + duration
        );


        param.linearRampToValueAtTime(
            0,
            time + duration + this.release
        );


    }


}