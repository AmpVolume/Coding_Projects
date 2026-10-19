export class Selection {


    selectedNotes:string[];


    constructor(){

        this.selectedNotes=[];

    }



    select(id:string){

        if(
            !this.selectedNotes.includes(id)
        ){

            this.selectedNotes.push(id);

        }

    }



    deselect(id:string){

        this.selectedNotes =
        this.selectedNotes.filter(
            x=>x!==id
        );

    }



    clear(){

        this.selectedNotes=[];

    }



    contains(id:string){

        return this.selectedNotes.includes(id);

    }



}