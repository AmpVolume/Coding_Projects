import { Song } from "../model/Song";
import { JsonSerializer } from "./JsonSerializer";



export class SongLoader {



    static load(
        file:File
    ):Promise<Song>{



        return new Promise(
            (resolve,reject)=>{


                const reader =
                new FileReader();



                reader.onload =
                ()=>{


                    try{


                        const json =
                        reader.result
                        as string;



                        const data =
                        JsonSerializer.deserialize<Song>(
                            json
                        );



                        resolve(
                            data
                        );


                    }
                    catch(error){

                        reject(
                            error
                        );

                    }


                };




                reader.onerror =
                ()=>{


                    reject(
                        reader.error
                    );


                };




                reader.readAsText(
                    file
                );


            }
        );


    }



}