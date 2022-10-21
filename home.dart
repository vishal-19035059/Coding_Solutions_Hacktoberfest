import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:pusher_channels_flutter/pusher_channels_flutter.dart';
import 'secrets.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String userName = 'Anonymous';
  String get authURL => "${_hostname()}/pusher/auth/$userName";
  String channelName = 'presence-my-channel';

  Future<void> _initPusher() async {
    try {
      PusherChannelsFlutter pusher = PusherChannelsFlutter.getInstance();
      await pusher.init(
        apiKey: apikey,
        // Place Your own Api Key
        cluster: cluster,
        // Place Your own Cluster
        onConnectionStateChange: onConnectionStateChange,
        onAuthorizer: onAuthorizer,
        useTLS: true,
        authEndpoint: authURL,
      );

      await pusher.subscribe(
        channelName: channelName,
        onSubscriptionSucceeded: (data) {
          onSubscriptionSucceeded(channelName, data);
        },
        onSubscriptionError: (message, e) {
          onSubscriptionError(message, e);
        },
        onEvent: (event) {
          onEvent(event);
        },
      );
      await pusher.connect();
    } catch (e) {
      if (kDebugMode) {
        print("Error: $e");
      }
    }
  }

  void onConnectionStateChange(dynamic currentState, dynamic previousState) {
    if (kDebugMode) {
      print("Connection: $currentState");
    }
  }

  String _hostname() {
    if (kIsWeb) {
      return 'http://localhost:5000';
    } else {
      if (Platform.isAndroid) {
        return 'http://10.0.2.2:5000';
      } else {
        return 'http://localhost:5000';
      }
    }
  }

  dynamic onAuthorizer(
      String channelName, String socketId, dynamic options) async {
    var result = await post(
      Uri.parse(authURL),
      headers: {"Content-Type": "application/x-www-form-urlencoded"},
      body: {
        "socket_id": socketId,
        "channel_name": channelName,
      },
    );
    return jsonDecode(result.body);
  }

  void onSubscriptionSucceeded(String channelName, dynamic data) {
    if (kDebugMode) {
      print("onSubscriptionSucceeded: $channelName data: $data");
    }
  }

  void onSubscriptionError(String message, dynamic e) {
    if (kDebugMode) {
      print("onSubscriptionError: $message Exception: $e");
    }
  }

  void onEvent(PusherEvent event) {
    if (kDebugMode) {
      print("Event Received: ${event.data}");
      print("Event name: ${event.eventName}");
    }
  }

  @override
  void initState() {
    super.initState();
    _initPusher();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: Text('Current Time: ${DateTime.now().toLocal()}'),
        ),
      ),
    );
  }
}
