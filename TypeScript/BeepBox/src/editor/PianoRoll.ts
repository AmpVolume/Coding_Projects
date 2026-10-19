import { Pattern } from "../model/Pattern";
import { Note } from "../model/Note";


export class PianoRoll {



    pattern?:Pattern;



    selectPattern(
        pattern:Pattern
    ){

        this.pattern=pattern;

    }





    addNote(
        note:Note
    ){

        if(!this.pattern)
            return;


        this.pattern.addNote(
            note
        );

    }





    deleteNote(
        id:string
    ){

        if(!this.pattern)
            return;


        this.pattern.removeNote(
            id
        );

    }





}