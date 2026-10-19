export class Slider {


    element:HTMLInputElement;



    constructor(
        min:number,
        max:number,
        value:number
    ){


        this.element =
        document.createElement(
            "input"
        );


        this.element.type =
        "range";


        this.element.min =
        String(min);


        this.element.max =
        String(max);


        this.element.value =
        String(value);


    }





    getValue():number{


        return Number(
            this.element.value
        );


    }





    onChange(
        callback:(value:number)=>void
    ){

        this.element.oninput =
        ()=>{


            callback(
                this.getValue()
            );


        };


    }





    mount(
        parent:HTMLElement
    ){

        parent.appendChild(
            this.element
        );

    }



}