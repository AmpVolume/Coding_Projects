export class Button {


    element:HTMLButtonElement;



    constructor(
        text:string
    ){

        this.element =
        document.createElement(
            "button"
        );


        this.element.innerText =
        text;

    }





    onClick(
        callback:()=>void
    ){

        this.element.onclick =
        callback;

    }





    mount(
        parent:HTMLElement
    ){

        parent.appendChild(
            this.element
        );

    }


}