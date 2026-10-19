import { UndoManager } from "../commands/UndoManager";
import { ICommand } from "../commands/ICommand";


export class History {



    manager:UndoManager;




    constructor(){

        this.manager =
        new UndoManager();

    }





    execute(
        command:ICommand
    ){

        this.manager.execute(
            command
        );

    }





    undo(){

        this.manager.undo();

    }





    redo(){

        this.manager.redo();

    }



}