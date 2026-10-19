import { SongDocument } from "./SongDocument";
import { PatternEditor } from "./PatternEditor";
import { PianoRoll } from "./PianoRoll";
import { InstrumentEditor } from "./InstrumentEditor";


export class SongEditor {



    document:SongDocument;


    pianoRoll:PianoRoll;


    patternEditor:PatternEditor;


    instrumentEditor:InstrumentEditor;




    constructor(
        document:SongDocument
    ){

        this.document=document;



        this.pianoRoll =
        new PianoRoll();



        this.patternEditor =
        new PatternEditor();



        this.instrumentEditor =
        new InstrumentEditor();


    }





    update(){

        // editor refresh loop

    }




}