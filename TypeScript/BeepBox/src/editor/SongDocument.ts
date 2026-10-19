import { Song } from "../model/Song";
import { Selection } from "../model/Selection";


export class SongDocument {


    song:Song;


    selection:Selection;


    modified:boolean;



    constructor(
        song:Song
    ){

        this.song=song;

        this.selection =
        new Selection();


        this.modified=false;

    }




    markChanged(){

        this.modified=true;

    }





    save(){

        this.modified=false;

    }




}