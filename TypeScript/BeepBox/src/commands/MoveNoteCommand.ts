import { ICommand } from "./ICommand";
import { Note } from "../model/Note";



export class MoveNoteCommand implements ICommand {



    note:Note;



    oldStart:number;


    newStart:number;




    constructor(
        note:Note,
        newStart:number
    ){

        this.note=note;


        this.oldStart =
        note.start;


        this.newStart =
        newStart;

    }





    execute(){

        this.note.start =
        this.newStart;

    }





    undo(){

        this.note.start =
        this.oldStart;

    }



}