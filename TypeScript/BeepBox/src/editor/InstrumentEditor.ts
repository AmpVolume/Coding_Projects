import { Instrument } from "../model/Instrument";


export class InstrumentEditor {


    instrument?:Instrument;



    load(
        instrument:Instrument
    ){

        this.instrument =
        instrument;

    }





    setVolume(
        value:number
    ){

        if(this.instrument)
        {

            this.instrument.volume =
            value;

        }

    }





    setWaveform(
        waveform:
        "sine"|
        "square"|
        "triangle"|
        "sawtooth"
    ){

        if(this.instrument)
        {

            this.instrument.waveform =
            waveform;

        }

    }


}