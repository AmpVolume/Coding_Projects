import { Mixer } from "./Mixer";
import { Synth } from "./Synth";
import { Effects } from "./Effects";


export class AudioEngine {


    context:AudioContext;


    mixer:Mixer;


    synth:Synth;


    effects:Effects;



    constructor(){


        this.context =
        new AudioContext();



        this.mixer =
        new Mixer(
            this.context
        );



        this.synth =
        new Synth(
            this.context
        );



        this.effects =
        new Effects(
            this.context
        );


        this.synth.output.connect(
            this.mixer.master
        );

    }





    start(){

        if(
            this.context.state==="suspended"
        ){

            this.context.resume();

        }

    }




    stop(){

        this.context.suspend();

    }




    playNote(
        pitch:number,
        duration:number
    ){

        this.start();


        this.synth.playNote(
            pitch,
            duration
        );

    }



}