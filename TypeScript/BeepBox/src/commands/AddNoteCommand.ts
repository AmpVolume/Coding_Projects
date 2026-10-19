import { ICommand } from "./ICommand";
import { Pattern } from "../model/Pattern";
import { Note } from "../model/Note";


export class AddNoteCommand implements ICommand {


    pattern:Pattern;

    note:Note;



    constructor(
        pattern:Pattern,
        note:Note
    ){

        this.pattern=pattern;

        this.note=note;

    }





    execute(){

        this.pattern.addNote(
            this.note
        );

    }






    undo(){

        this.pattern.removeNote(
            this.note.id
        );

    }



}