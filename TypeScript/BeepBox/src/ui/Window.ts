import { Theme } from "./Theme";


export class Window {


    element:HTMLDivElement;


    theme:Theme;



    constructor(
        title:string
    ){


        this.theme =
        new Theme();



        this.element =
        document.createElement(
            "div"
        );



        const header =
        document.createElement(
            "h2"
        );


        header.innerText =
        title;



        this.element.appendChild(
            header
        );



        this.theme.apply(
            this.element
        );


    }





    add(
        child:HTMLElement
    ){

        this.element.appendChild(
            child
        );

    }





    mount(
        parent:HTMLElement
    ){

        parent.appendChild(
            this.element
        );

    }



}