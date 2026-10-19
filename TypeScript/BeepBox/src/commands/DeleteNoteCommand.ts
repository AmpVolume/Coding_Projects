import { ICommand } from "./ICommand";
import { Pattern } from "../model/Pattern";
import { Note } from "../model/Note";



export class DeleteNoteCommand implements ICommand {


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

        this.pattern.removeNote(
            this.note.id
        );

    }






    undo(){

        this.pattern.addNote(
            this.note
        );

    }



}