import { ICommand } from "./ICommand";



export class UndoManager {



    undoStack:ICommand[];


    redoStack:ICommand[];





    constructor(){

        this.undoStack=[];

        this.redoStack=[];

    }





    execute(
        command:ICommand
    ){


        command.execute();



        this.undoStack.push(
            command
        );



        this.redoStack=[];


    }





    undo(){


        const command =
        this.undoStack.pop();



        if(!command)
            return;



        command.undo();



        this.redoStack.push(
            command
        );


    }





    redo(){


        const command =
        this.redoStack.pop();



        if(!command)
            return;



        command.execute();



        this.undoStack.push(
            command
        );


    }







    clear(){

        this.undoStack=[];

        this.redoStack=[];

    }




}