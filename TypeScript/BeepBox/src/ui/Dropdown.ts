export class Dropdown {


    element:HTMLSelectElement;



    constructor(
        options:string[]
    ){


        this.element =
        document.createElement(
            "select"
        );



        for(
            const option of options
        ){

            const item =
            document.createElement(
                "option"
            );


            item.text =
            option;


            this.element.add(
                item
            );


        }


    }





    getValue(){

        return this.element.value;

    }





    onChange(
        callback:(value:string)=>void
    ){

        this.element.onchange =
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