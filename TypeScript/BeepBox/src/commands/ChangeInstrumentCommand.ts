import { ICommand } from "./ICommand";
import { Channel } from "../model/Channel";
import { Instrument } from "../model/Instrument";



export class ChangeInstrumentCommand implements ICommand {



    channel:Channel;


    oldInstrument:Instrument;


    newInstrument:Instrument;





    constructor(
        channel:Channel,
        instrument:Instrument
    ){

        this.channel=channel;


        this.oldInstrument =
        channel.instrument;


        this.newInstrument =
        instrument;


    }






    execute(){

        this.channel.instrument =
        this.newInstrument;

    }






    undo(){

        this.channel.instrument =
        this.oldInstrument;

    }



}