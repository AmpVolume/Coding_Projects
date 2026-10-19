import { Song } from "../model/Song";
import { JsonSerializer } from "./JsonSerializer";



export class SongSaver {



    static save(
        song:Song
    ){


        const json =
        JsonSerializer.serialize(
            song
        );



        const blob =
        new Blob(
            [
                json
            ],
            {
                type:
                "application/json"
            }
        );



        const url =
        URL.createObjectURL(
            blob
        );



        const link =
        document.createElement(
            "a"
        );



        link.href=url;



        link.download =
        `${song.name}.ultra`;



        link.click();



        URL.revokeObjectURL(
            url
        );


    }



}