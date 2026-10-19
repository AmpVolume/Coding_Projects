import { Channel } from "../model/Channel";
import { Pattern } from "../model/Pattern";


export class PatternEditor {



    channel?:Channel;




    setChannel(
        channel:Channel
    ){

        this.channel=channel;

    }





    createPattern(
        id:string,
        name:string
    ){


        if(!this.channel)
            return;



        const pattern =
        new Pattern(
            id,
            name
        );



        this.channel.addPattern(
            pattern
        );



        return pattern;


    }




}