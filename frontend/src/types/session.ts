export interface IFetchSession {
  id: number,
  name: string,
  desc: string,
  creation_datetime: number,
  images: {
    session_id: number,
    name: string,
    creation_datetime: number,
    token: string,
    classes: string
  }
}
