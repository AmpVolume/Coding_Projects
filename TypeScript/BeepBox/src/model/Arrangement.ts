export interface ArrangementSection {

    name:string;

    start:number;

    length:number;

    patternIds:string[];

}



export class Arrangement {


    sections:ArrangementSection[];


    constructor(){

        this.sections=[];

    }



    addSection(
        section:ArrangementSection
    ){

        this.sections.push(section);

    }



    removeSection(name:string){

        this.sections =
        this.sections.filter(
            s=>s.name!==name
        );

    }


}