export enum InstrumentType {

    SYNTH = "synth",
    DRUM = "drum",
    SAMPLE = "sample"

}



export class Instrument {

    id: string;

    name: string;

    type: InstrumentType;


    volume: number;

    pan: number;


    waveform:
    "sine" |
    "square" |
    "triangle" |
    "sawtooth";


    constructor(
        id: string,
        name: string,
        type: InstrumentType = InstrumentType.SYNTH
    ){

        this.id = id;
        this.name = name;
        this.type = type;


        this.volume = 1;
        this.pan = 0;


        this.waveform = "sine";
    }


}