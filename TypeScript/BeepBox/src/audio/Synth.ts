import { Oscillator } from "./Oscillator";
import { Envelope } from "./Envelope";


export class Synth {


    context:AudioContext;


    oscillator:
    Oscillator;


    envelope:
    Envelope;



    output:
    GainNode;



    waveform:
    OscillatorType;



    constructor(
        context:AudioContext
    ){

        this.context=context;


        this.oscillator =
        new Oscillator(context);


        this.envelope =
        new Envelope();



        this.output =
        context.createGain();


        this.output.gain.value=1;



        this.waveform="sine";

    }





    playNote(
        midi:number,
        duration:number
    ){


        const osc =
        this.oscillator.create(
            this.oscillator.midiToFrequency(midi),
            this.waveform
        );



        const gain =
        this.context.createGain();



        osc.connect(
            gain
        );


        gain.connect(
            this.output
        );



        const now =
        this.context.currentTime;



        this.envelope.apply(
            gain,
            now,
            duration
        );



        osc.start(now);


        osc.stop(
            now +
            duration +
            this.envelope.release
        );


    }



}