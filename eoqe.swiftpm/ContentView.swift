//
//  ContentView.swift
//  eoqe
//
//  Created by Keshav Khaneja on 4/7/22.
//


import SwiftUI
import AVKit

struct ContentView: View {

    var _prerenders = ["DNEVqn25sUgekQIA", "65y3k3Yu5gLvbbbs", "QFHjRVng3bGK94TV", "p3CWAcsgzdgfQF57", "mfgAH26XeqpfCs9c", "kcHjCv3pRCDPV2YY", "Ms5AcqTrMtVr4NES", "tqVB5XPuADC7sAzc", "Ff2SfV4eepc8DMP4", "JK23fV4epubicJO1P"]
    
    let delay = [2.36, 9.26, 10.26, 0, 17.56, 9.26, 40.36, 4.93]

    @Environment(\.colorScheme) var colorScheme
    @State private var opacityNextButton = 0.0
    @State private var screenIndex = 0
    @State private var orientation = UIDeviceOrientation.unknown
    @State private var showingAlert = false
    
    @State var audioPlayer: AVAudioPlayer!
    @State var downRadius: Double = 120
    @State var graph: String = "graph"
    @State var isShown = false

    struct Parabola: Shape {
        @State var downRadius: Double
        var value: CGFloat
        func path(in rect: CGRect) -> Path {
            Path { path in
                let center = rect.width / 2
                let downRadius: CGFloat = (downRadius * value) - 45
                path.move(to: CGPoint(x: center - 150, y: 0))
                let to1 = CGPoint (x: center, y: downRadius)
                let control1 = CGPoint (x: center - 145, y: 0)
                let control2 = CGPoint (x: center - 80, y: downRadius)
                let to2 = CGPoint(x: center + 150, y: 0)
                let control3 = CGPoint (x: center + 80, y: downRadius)
                let control4 = CGPoint (x: center + 145, y: 0)

                path.addCurve(to: to1, control1: control1, control2: control2)
                path.addCurve(to: to2, control1: control3, control2: control4)

            }
        }
    }
    
    var body: some View {
        ZStack {
            Color.black
                .ignoresSafeArea()
            switch screenIndex {
            case 0:
                screen0
            case 1:
                screen1
            case 2:
                screen2
            case 3:
                screen3
            case 4:
                screen4a
            case 5:
                screen5
            case 6:
                screen6
            case 7:
                screen7
            case 8:
                GeometryReader { bodyView in
                    VStack {
                        if isShown {
                            ZStack{
                                if UIDevice.current.orientation.isPortrait {
                                    Image("giraph")
                                         .resizable()
                                         .aspectRatio(contentMode: .fit)
                                         .frame(width: bodyView.size.width*1, height: bodyView.size.height*0.8)
                                         .scaledToFit()
                                         .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                                } else {
                                    Image("graph")
                                         .resizable()
                                         .aspectRatio(contentMode: .fit)
                                         .frame(width: bodyView.size.width*1, height: bodyView.size.height*0.8)
                                             .scaledToFit()
                                             .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                                    
                                    HStack {
                                        Parabola(downRadius: downRadius,value: 5)
                                            .stroke(Color.yellow, lineWidth: 3.5)
                                            .aspectRatio(contentMode: .fit)
                                            .frame(width: bodyView.size.width*1, height: bodyView.size.height*0.8)
                                            .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 120)

                                    }.frame(width: bodyView.size.width*1, height: bodyView.size.height*0.77)
                                        .scaledToFit()
                                        .clipped()
                                        .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 58)
                                }
                            }
                            HStack{
                                Slider(value: $downRadius, in: -70...200)
                                    .accentColor(.teal)
                                    .padding(60)
                                nextButton
                            }
                        }
                    }.animation(Animation.easeInOut(duration: 1).delay(0.5))
                    .onAppear() {
                        self.isShown.toggle()
                        opacityNextButton = 1
                   }
                }
            case 9:
                screen9
            default:
                screen0
            }
        }
    }
    

    private let player0: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "DNEVqn25sUgekQIA", ofType: "mp4")!))
    
    var screen0: some View {
        GeometryReader { bodyView in
            VStack {
                PlayerView(player: self.player0)
                    .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                nextButton
            }.onAppear {
                animationStarts_0()
                // music
                let sound = Bundle.main.path(forResource: "Reflections", ofType: "mp3")
                self.audioPlayer = try! AVAudioPlayer(contentsOf: URL(fileURLWithPath: sound!))
                self.audioPlayer.play()
                self.audioPlayer.volume = 0.8
                DispatchQueue.main.asyncAfter(deadline: .now() + delay[0]) {
                    withAnimation {
                        opacityNextButton = 1
                    }
                }
            }
        }
    }

    private let player1: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "65y3k3Yu5gLvbbbs", ofType: "mp4")!))
    private let player2: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "QFHjRVng3bGK94TV", ofType: "mp4")!))
    
    var screen1: some View {
        GeometryReader { bodyView in
            VStack {
                PlayerView(player: self.player1)
                    .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                nextButton
            }.onAppear {
                animationStarts_1()
                DispatchQueue.main.asyncAfter(deadline: .now() + delay[1]) {
                    withAnimation {
                        opacityNextButton = 1
                    }
                }
            }
        }
    }
    
    var screen2: some View {
        GeometryReader { bodyView in
            VStack {
                ZStack{
                    Image("still1")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(width: bodyView.size.width*1, height: bodyView.size.height*0.8)
                        .scaledToFit()
                        .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                    PlayerView(player: self.player2)
                        .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                }
                nextButton
            }.onAppear {
                animationStarts_2()
                DispatchQueue.main.asyncAfter(deadline: .now() + delay[2]) {
                    withAnimation {
                        opacityNextButton = 1
                    }
                }
            }
        }
    }
    
    private let player3: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "p3CWAcsgzdgfQF57", ofType: "mp4")!))
    private let player4a: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "mfgAH26XeqpfCs9c", ofType: "mp4")!))
    private let player4b: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "kcHjCv3pRCDPV2YY", ofType: "mp4")!))

    var screen3: some View {
        GeometryReader { bodyView in
            VStack {
            ZStack{
                Image("still2")
                     .resizable()
                     .aspectRatio(contentMode: .fit)
                     .frame(width: bodyView.size.width*1, height: bodyView.size.height*0.8)
                         .scaledToFit()
                         .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                
                PlayerView(player: self.player3)
                    .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                
                HStack {
                    Button {
                        UserDefaults.standard.set(true, forKey: "dyeq")
                        screenIndex = screenIndex + 1
                    } label: {
                    Text("6x^2 - 12x + 3")
                        .font(Font.custom(cmuSerif, size: 40))
                        .foregroundColor(.white)
                        .padding(.bottom, 60)
                        .frame(width: bodyView.size.width*0.35, height: 130, alignment: .leading)
                        .padding(.leading, 65)
                        .background(Color.blue)
                        .opacity(0)
                    }
                    Spacer()
                           .frame(width: bodyView.size.width*0.05)
                    Button {
                        UserDefaults.standard.set(false, forKey: "dyeq")
                        screenIndex = screenIndex + 1
                    } label: {
                    Text("x^2 + 2.4x - 1")
                        .font(Font.custom(cmuSerif, size: 40))
                        .foregroundColor(.white)
                        .padding(.bottom, 60)
                        .frame(width: bodyView.size.width*0.35, height: 130, alignment: .trailing)
                        .padding(.leading, 65)
                        .background(Color.blue)
                        .opacity(0)
                    }
                }.frame(width: bodyView.size.width, height: 100)
            }
            nextButton
            }.onAppear {
                animationStarts_3()
            }
        }
    }
    
    var screen4a: some View {
        GeometryReader { bodyView in
            VStack {
                if UserDefaults.standard.bool(forKey: "dyeq") {
                    PlayerView(player: self.player4a)
                        .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                } else if !UserDefaults.standard.bool(forKey: "dyeq") {
                    PlayerView(player: self.player4b)
                        .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                }
                nextButton
            }.onAppear {
                if UserDefaults.standard.bool(forKey: "dyeq") { animationStarts_4a() }
                else if !UserDefaults.standard.bool(forKey: "dyeq") { animationStarts_4b() }
                DispatchQueue.main.asyncAfter(deadline: .now() + delay[4]) {
                    withAnimation {
                        opacityNextButton = 1
                    }
                }
            }
        }
    }
    
    private let player5: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "Ms5AcqTrMtVr4NES", ofType: "mp4")!))
    private let player6: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "tqVB5XPuADC7sAzc", ofType: "mp4")!))
    private let player7: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "Ff2SfV4eepc8DMP4", ofType: "mp4")!))
    var screen5: some View {
        GeometryReader { bodyView in
            VStack {
                PlayerView(player: self.player5)
                    .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                nextButton
            }.onAppear {
                opacityNextButton = 0
                animationStarts_5()
                DispatchQueue.main.asyncAfter(deadline: .now() + delay[5]) {
                    withAnimation {
                        opacityNextButton = 1
                    }
                }
            }
        }
    }
    
    var screen6: some View {
        GeometryReader { bodyView in
            VStack {
                PlayerView(player: self.player6)
                    .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                nextButton
            }.onAppear {
                opacityNextButton = 0
                animationStarts_6()
                DispatchQueue.main.asyncAfter(deadline: .now() + delay[6]) {
                    withAnimation {
                        opacityNextButton = 1
                    }
                }
            }
        }
    }
    
    private let player9: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "JK23fV4epubicJO1P", ofType: "mp4")!))
    var screen7: some View {
        GeometryReader { bodyView in
            VStack {
                PlayerView(player: self.player7)
                    .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                nextButton
            }.onAppear {
                opacityNextButton = 0
                animationStarts_7()
                DispatchQueue.main.asyncAfter(deadline: .now() + delay[7]) {
                    withAnimation {
                        opacityNextButton = 1
                    }
                }
            }
        }
    }
    
    var screen9: some View {
        GeometryReader { bodyView in
            VStack {
                PlayerView(player: self.player9)
                    .position(x: bodyView.size.width / 2, y: (bodyView.size.height / 2) - 54)
                nextButton
            }.onAppear {
                    animationStarts_9()
                }
            }
        }

    var nextButton: some View {
        Button {
            if opacityNextButton == 0 {
            } else {
                screenIndex = screenIndex + 1
                opacityNextButton = 0
            }
            
        } label: {
            Text("Click to continue")
                .font(Font.custom(cmuSerif, size: 42))
                .foregroundColor(.white)
                .padding(48)
                .opacity(opacityNextButton)
        }
    }
    
    private func animationStarts_0() {
        self.player0.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player0.play()
    }
    
    private func animationStarts_1() {
        self.player1.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player1.play()
    }
    
    private func animationStarts_2() {
        self.player2.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player2.play()
    }
    
    private func animationStarts_3() {
        self.player3.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player3.play()
    }
    
    private func animationStarts_4a() {
        self.player4a.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player4a.play()
    }
    
    private func animationStarts_4b() {
        self.player4b.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player4b.play()
    }
    
    private func animationStarts_5() {
        self.player5.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player5.play()
    }
    
    private func animationStarts_6() {
        self.player6.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player6.play()
    }
    private func animationStarts_7() {
        self.player7.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player7.play()
    }
    
    private func animationStarts_9() {
        self.player9.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player9.play()
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .previewInterfaceOrientation(.landscapeRight)
    }
}

struct PlayerView: UIViewRepresentable {
    let player: AVPlayer

    func updateUIView(_ uiView: UIView, context: UIViewRepresentableContext<PlayerView>) {
    }

    func makeUIView(context: Context) -> UIView {
        return PlayerUIView(player: player)
    }
}

struct DeviceRotationViewModifier: ViewModifier {
    let action: (UIDeviceOrientation) -> Void
    func body(content: Content) -> some View {
        content
            .onAppear()
            .onReceive(NotificationCenter.default.publisher(for: UIDevice.orientationDidChangeNotification)) { _ in
                action(UIDevice.current.orientation)
            }
    }
}

extension View {
    func onRotate(perform action: @escaping (UIDeviceOrientation) -> Void) -> some View {
        self.modifier(DeviceRotationViewModifier(action: action))
    }
}
