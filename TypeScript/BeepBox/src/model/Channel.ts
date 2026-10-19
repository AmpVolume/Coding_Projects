import { Pattern } from "./Pattern";
import { Instrument } from "./Instrument";


export class Channel {


    id:string;

    name:string;


    instrument:Instrument;


    patterns:Pattern[];



    muted:boolean;

    solo:boolean;



    constructor(
        id:string,
        name:string,
        instrument:Instrument
    ){

        this.id=id;
        this.name=name;

        this.instrument=instrument;

        this.patterns=[];

        this.muted=false;
        this.solo=false;

    }




    addPattern(pattern:Pattern){

        this.patterns.push(pattern);

    }




    removePattern(id:string){

        this.patterns =
        this.patterns.filter(
            p=>p.id!==id
        );

    }



}