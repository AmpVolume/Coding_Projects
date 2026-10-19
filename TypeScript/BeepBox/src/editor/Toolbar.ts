export class Toolbar {



    buttons:string[];




    constructor(){

        this.buttons=[

            "New",
            "Open",
            "Save",
            "Undo",
            "Redo"

        ];

    }





    click(
        button:string
    ){

        console.log(
            "Toolbar:",
            button
        );

    }



}