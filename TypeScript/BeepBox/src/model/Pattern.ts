import { Note } from "./Note";


export class Pattern {

    id: string;
    name: string;

    length: number;

    notes: Note[];


    constructor(
        id: string,
        name: string,
        length: number = 4
    ) {

        this.id = id;
        this.name = name;
        this.length = length;

        this.notes = [];
    }



    addNote(note: Note): void {
        this.notes.push(note);
    }



    removeNote(id: string): void {

        this.notes =
            this.notes.filter(
                note => note.id !== id
            );

    }



    getNotes(): Note[] {
        return this.notes;
    }



    clone(): Pattern {

        const pattern =
            new Pattern(
                this.id,
                this.name,
                this.length
            );


        pattern.notes =
            this.notes.map(
                note => note.clone()
            );


        return pattern;
    }

}