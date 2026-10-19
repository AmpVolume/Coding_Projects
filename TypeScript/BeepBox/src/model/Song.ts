import { Channel } from "./Channel";
import { Timeline } from "./Timeline";
import { Arrangement } from "./Arrangement";


export class Song {


    id:string;

    name:string;


    channels:Channel[];


    timeline:Timeline;


    arrangement:Arrangement;



    constructor(
        id:string,
        name:string
    ){

        this.id=id;
        this.name=name;


        this.channels=[];


        this.timeline =
        new Timeline();



        this.arrangement =
        new Arrangement();

    }




    addChannel(
        channel:Channel
    ){

        this.channels.push(channel);

    }




    removeChannel(
        id:string
    ){

        this.channels =
        this.channels.filter(
            c=>c.id!==id
        );

    }




    getLength():number{

        let length=0;


        for(
            const channel of this.channels
        ){

            for(
                const pattern of channel.patterns
            ){

                if(pattern.length > length)
                    length=pattern.length;

            }

        }


        return length;

    }



}