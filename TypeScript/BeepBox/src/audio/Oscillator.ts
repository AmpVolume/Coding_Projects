export type Waveform =
    | "sine"
    | "square"
    | "triangle"
    | "sawtooth";


export class Oscillator {


    context: AudioContext;


    constructor(context: AudioContext){

        this.context = context;

    }



    create(
        frequency:number,
        waveform:Waveform = "sine"
    ):OscillatorNode{


        const oscillator =
            this.context.createOscillator();



        oscillator.type =
            waveform;



        oscillator.frequency.value =
            frequency;



        return oscillator;

    }



    midiToFrequency(
        midi:number
    ):number{


        return 440 *
        Math.pow(
            2,
            (midi-69)/12
        );

    }


}